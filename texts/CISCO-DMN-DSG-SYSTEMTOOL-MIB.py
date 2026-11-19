#
# PySNMP MIB module CISCO-DMN-DSG-SYSTEMTOOL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-DMN-DSG-SYSTEMTOOL-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 14:35:13 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint")
ciscoDSGUtilities, = mibBuilder.importSymbols("CISCO-DMN-DSG-ROOT-MIB", "ciscoDSGUtilities")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Integer32, Gauge32, MibIdentifier, NotificationType, Unsigned32, Counter64, ObjectIdentity, IpAddress, iso, Counter32, ModuleIdentity, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Integer32", "Gauge32", "MibIdentifier", "NotificationType", "Unsigned32", "Counter64", "ObjectIdentity", "IpAddress", "iso", "Counter32", "ModuleIdentity", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoDSGSystemTool = ModuleIdentity((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 8))
ciscoDSGSystemTool.setRevisions(('2010-08-03 09:00', '2009-12-20 15:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoDSGSystemTool.setRevisionsDescriptions(('V01.00.01 2010-08-03\n                    Item systemToolClearLogs is added.', 'V01.00.00 2009-12-20\n                    Initial Version.',))
if mibBuilder.loadTexts: ciscoDSGSystemTool.setLastUpdated('201008030900Z')
if mibBuilder.loadTexts: ciscoDSGSystemTool.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoDSGSystemTool.setContactInfo('Cisco Systems, Inc.\n            Customer Service\n            Postal: 170 W Tasman Drive\n            San Jose, CA 95134\n            USA\n            Tel: +1 800 553 NETS\n\n            E-mail: cs-ipsla@cisco.com')
if mibBuilder.loadTexts: ciscoDSGSystemTool.setDescription('Cisco DSG System Tool MIB.')
systemTool = MibIdentifier((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 8, 1))
systemToolBanner = MibScalar((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 8, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disable", 1), ("enable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: systemToolBanner.setStatus('current')
if mibBuilder.loadTexts: systemToolBanner.setDescription('Enable / Disable OSD Banner Messages.')
systemToolReboot = MibScalar((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 8, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("writeOnly", 1), ("yes", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: systemToolReboot.setStatus('current')
if mibBuilder.loadTexts: systemToolReboot.setDescription('Setting yes(2) reboots the system.')
systemToolFactoryReset = MibScalar((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 8, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("writeOnly", 1), ("yes", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: systemToolFactoryReset.setStatus('current')
if mibBuilder.loadTexts: systemToolFactoryReset.setDescription('Setting yes( 2 ) performs factory reset of the system.')
systemToolCleanUnusedTables = MibScalar((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 8, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("writeOnly", 1), ("yes", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: systemToolCleanUnusedTables.setStatus('current')
if mibBuilder.loadTexts: systemToolCleanUnusedTables.setDescription('Set this object to yes( 2 ) to clean up memory of parameters\n        unused by this version.')
systemToolCAMode = MibScalar((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 8, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("standard", 1), ("open", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: systemToolCAMode.setStatus('current')
if mibBuilder.loadTexts: systemToolCAMode.setDescription('Custom Tuning Mode: Conditional Access Mode: Standard/ Open.')
systemToolClearLogs = MibScalar((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 8, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("writeOnly", 1), ("yes", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: systemToolClearLogs.setStatus('current')
if mibBuilder.loadTexts: systemToolClearLogs.setDescription('Set this object to yes( 2 ) to clean up memory of logs.')
mibBuilder.exportSymbols("CISCO-DMN-DSG-SYSTEMTOOL-MIB", ciscoDSGSystemTool=ciscoDSGSystemTool, systemToolReboot=systemToolReboot, systemToolCAMode=systemToolCAMode, systemToolBanner=systemToolBanner, systemToolFactoryReset=systemToolFactoryReset, systemToolClearLogs=systemToolClearLogs, PYSNMP_MODULE_ID=ciscoDSGSystemTool, systemTool=systemTool, systemToolCleanUnusedTables=systemToolCleanUnusedTables)
