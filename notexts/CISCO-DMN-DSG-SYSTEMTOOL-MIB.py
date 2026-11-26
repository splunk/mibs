#
# PySNMP MIB module CISCO-DMN-DSG-SYSTEMTOOL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-DMN-DSG-SYSTEMTOOL-MIB
# Produced by pysmi-1.1.12 at Thu Nov 26 06:06:58 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoDSGUtilities, = mibBuilder.importSymbols("CISCO-DMN-DSG-ROOT-MIB", "ciscoDSGUtilities")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Counter64, TimeTicks, NotificationType, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, ModuleIdentity, IpAddress, Bits, Gauge32, Unsigned32, MibIdentifier, Counter32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "NotificationType", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "ModuleIdentity", "IpAddress", "Bits", "Gauge32", "Unsigned32", "MibIdentifier", "Counter32", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoDSGSystemTool = ModuleIdentity((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 8))
ciscoDSGSystemTool.setRevisions(('2010-08-03 09:00', '2009-12-20 15:00',))
if mibBuilder.loadTexts: ciscoDSGSystemTool.setLastUpdated('201008030900Z')
if mibBuilder.loadTexts: ciscoDSGSystemTool.setOrganization('Cisco Systems, Inc.')
systemTool = MibIdentifier((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 8, 1))
systemToolBanner = MibScalar((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 8, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disable", 1), ("enable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: systemToolBanner.setStatus('current')
systemToolReboot = MibScalar((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 8, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("writeOnly", 1), ("yes", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: systemToolReboot.setStatus('current')
systemToolFactoryReset = MibScalar((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 8, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("writeOnly", 1), ("yes", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: systemToolFactoryReset.setStatus('current')
systemToolCleanUnusedTables = MibScalar((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 8, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("writeOnly", 1), ("yes", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: systemToolCleanUnusedTables.setStatus('current')
systemToolCAMode = MibScalar((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 8, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("standard", 1), ("open", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: systemToolCAMode.setStatus('current')
systemToolClearLogs = MibScalar((1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 8, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("writeOnly", 1), ("yes", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: systemToolClearLogs.setStatus('current')
mibBuilder.exportSymbols("CISCO-DMN-DSG-SYSTEMTOOL-MIB", systemToolCAMode=systemToolCAMode, systemToolClearLogs=systemToolClearLogs, systemToolReboot=systemToolReboot, systemTool=systemTool, PYSNMP_MODULE_ID=ciscoDSGSystemTool, systemToolFactoryReset=systemToolFactoryReset, systemToolCleanUnusedTables=systemToolCleanUnusedTables, ciscoDSGSystemTool=ciscoDSGSystemTool, systemToolBanner=systemToolBanner)
