#
# PySNMP MIB module CISCO-DMN-DSG-BISS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-DMN-DSG-BISS-MIB
# Produced by pysmi-1.1.12 at Thu Nov 26 06:07:44 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ciscoDSGUtilities, = mibBuilder.importSymbols("CISCO-DMN-DSG-ROOT-MIB", "ciscoDSGUtilities")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, ModuleIdentity, TimeTicks, MibIdentifier, iso, Counter32, IpAddress, Integer32, NotificationType, ObjectIdentity, Unsigned32, Bits, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "ModuleIdentity", "TimeTicks", "MibIdentifier", "iso", "Counter32", "IpAddress", "Integer32", "NotificationType", "ObjectIdentity", "Unsigned32", "Bits", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoDSGBISS = ModuleIdentity((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 38))
ciscoDSGBISS.setRevisions(('2010-08-02 07:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoDSGBISS.setRevisionsDescriptions(('V01.00.00 2010-08-02\n                    Initial Version.',))
if mibBuilder.loadTexts: ciscoDSGBISS.setLastUpdated('201008020700Z')
if mibBuilder.loadTexts: ciscoDSGBISS.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoDSGBISS.setContactInfo('Cisco Systems, Inc.\n        Customer Service\n        Postal: 170 W Tasman Drive\n        San Jose, CA 95134\n        USA\n        Tel: +1 800 553 NETS\n\n        E-mail: cs-ipsla@cisco.com')
if mibBuilder.loadTexts: ciscoDSGBISS.setDescription('Cisco BISS MIB.')
bissMode = MibScalar((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 38, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("mode1", 1), ("modeE", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bissMode.setStatus('current')
if mibBuilder.loadTexts: bissMode.setDescription('BISS Mode Selection.')
bissMode1SessionWord = MibScalar((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 38, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 13))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bissMode1SessionWord.setStatus('current')
if mibBuilder.loadTexts: bissMode1SessionWord.setDescription('BISS Mode-1 Session Word.')
bissModeESessionWord = MibScalar((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 38, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 17))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bissModeESessionWord.setStatus('current')
if mibBuilder.loadTexts: bissModeESessionWord.setDescription('BISS Mode-E Encrypted Session Word.')
bissModeEInjectedId = MibScalar((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 38, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 15))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bissModeEInjectedId.setStatus('current')
if mibBuilder.loadTexts: bissModeEInjectedId.setDescription('BISS Mode-E Injected Id.')
mibBuilder.exportSymbols("CISCO-DMN-DSG-BISS-MIB", bissMode1SessionWord=bissMode1SessionWord, bissModeEInjectedId=bissModeEInjectedId, PYSNMP_MODULE_ID=ciscoDSGBISS, bissMode=bissMode, ciscoDSGBISS=ciscoDSGBISS, bissModeESessionWord=bissModeESessionWord)
