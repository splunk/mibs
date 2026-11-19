#
# PySNMP MIB module CISCO-DMN-DSG-BISS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-DMN-DSG-BISS-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 08:32:21 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoDSGUtilities, = mibBuilder.importSymbols("CISCO-DMN-DSG-ROOT-MIB", "ciscoDSGUtilities")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
ModuleIdentity, TimeTicks, IpAddress, Bits, ObjectIdentity, NotificationType, Gauge32, Counter64, Unsigned32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Integer32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "TimeTicks", "IpAddress", "Bits", "ObjectIdentity", "NotificationType", "Gauge32", "Counter64", "Unsigned32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Integer32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoDSGBISS = ModuleIdentity((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 38))
ciscoDSGBISS.setRevisions(('2010-08-02 07:00',))
if mibBuilder.loadTexts: ciscoDSGBISS.setLastUpdated('201008020700Z')
if mibBuilder.loadTexts: ciscoDSGBISS.setOrganization('Cisco Systems, Inc.')
bissMode = MibScalar((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 38, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("mode1", 1), ("modeE", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bissMode.setStatus('current')
bissMode1SessionWord = MibScalar((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 38, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 13))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bissMode1SessionWord.setStatus('current')
bissModeESessionWord = MibScalar((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 38, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 17))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bissModeESessionWord.setStatus('current')
bissModeEInjectedId = MibScalar((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 38, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 15))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bissModeEInjectedId.setStatus('current')
mibBuilder.exportSymbols("CISCO-DMN-DSG-BISS-MIB", bissMode1SessionWord=bissMode1SessionWord, bissModeEInjectedId=bissModeEInjectedId, bissModeESessionWord=bissModeESessionWord, PYSNMP_MODULE_ID=ciscoDSGBISS, bissMode=bissMode, ciscoDSGBISS=ciscoDSGBISS)
