#
# PySNMP MIB module CISCO-APPNAV-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-APPNAV-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 19 08:32:23 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
ModuleIdentity, TimeTicks, IpAddress, Bits, ObjectIdentity, NotificationType, Gauge32, Counter64, Unsigned32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Integer32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "TimeTicks", "IpAddress", "Bits", "ObjectIdentity", "NotificationType", "Gauge32", "Counter64", "Unsigned32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Integer32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoAppnavCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 610))
ciscoAppnavCapability.setRevisions(('2012-04-17 00:00',))
if mibBuilder.loadTexts: ciscoAppnavCapability.setLastUpdated('201204170000Z')
if mibBuilder.loadTexts: ciscoAppnavCapability.setOrganization('Cisco Systems, Inc.')
ciscoAppNavCapabilityWAASV5R0 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 610, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoAppNavCapabilityWAASV5R0 = ciscoAppNavCapabilityWAASV5R0.setProductRelease('OS=WAAS\n                     OSVERSION=V501')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoAppNavCapabilityWAASV5R0 = ciscoAppNavCapabilityWAASV5R0.setStatus('current')
mibBuilder.exportSymbols("CISCO-APPNAV-CAPABILITY", ciscoAppnavCapability=ciscoAppnavCapability, PYSNMP_MODULE_ID=ciscoAppnavCapability, ciscoAppNavCapabilityWAASV5R0=ciscoAppNavCapabilityWAASV5R0)
