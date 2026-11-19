#
# PySNMP MIB module CISCO-DMN-DSG-SYSTEMTOOL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-DMN-DSG-SYSTEMTOOL-MIB
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
mibBuilder.exportSymbols("CISCO-DMN-DSG-SYSTEMTOOL-MIB", systemToolFactoryReset=systemToolFactoryReset, ciscoDSGSystemTool=ciscoDSGSystemTool, systemToolClearLogs=systemToolClearLogs, systemToolReboot=systemToolReboot, systemTool=systemTool, PYSNMP_MODULE_ID=ciscoDSGSystemTool, systemToolCAMode=systemToolCAMode, systemToolCleanUnusedTables=systemToolCleanUnusedTables, systemToolBanner=systemToolBanner)
