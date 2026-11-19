#
# PySNMP MIB module CISCO-DMN-DSG-BISS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-DMN-DSG-BISS-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 14:34:42 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
ciscoDSGUtilities, = mibBuilder.importSymbols("CISCO-DMN-DSG-ROOT-MIB", "ciscoDSGUtilities")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
NotificationType, TimeTicks, IpAddress, ObjectIdentity, Unsigned32, Gauge32, ModuleIdentity, Integer32, Bits, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Counter64, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "TimeTicks", "IpAddress", "ObjectIdentity", "Unsigned32", "Gauge32", "ModuleIdentity", "Integer32", "Bits", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Counter64", "Counter32")
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
mibBuilder.exportSymbols("CISCO-DMN-DSG-BISS-MIB", ciscoDSGBISS=ciscoDSGBISS, PYSNMP_MODULE_ID=ciscoDSGBISS, bissModeESessionWord=bissModeESessionWord, bissMode=bissMode, bissMode1SessionWord=bissMode1SessionWord, bissModeEInjectedId=bissModeEInjectedId)
