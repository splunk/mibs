#
# PySNMP MIB module CISCO-AAA-SERVER-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-AAA-SERVER-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 19 08:32:21 2026
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
ciscoAAAServerCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 129))
ciscoAAAServerCapability.setRevisions(('2008-07-21 00:00', '2006-02-21 00:00', '2003-11-14 00:00', '2000-01-20 00:00',))
if mibBuilder.loadTexts: ciscoAAAServerCapability.setLastUpdated('200807210000Z')
if mibBuilder.loadTexts: ciscoAAAServerCapability.setOrganization('Cisco Systems, Inc.')
ciscoAAAServerCapabilityV10R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 129, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoAAAServerCapabilityV10R00 = ciscoAAAServerCapabilityV10R00.setProductRelease('Cisco IOS 12.0(4)XJ')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoAAAServerCapabilityV10R00 = ciscoAAAServerCapabilityV10R00.setStatus('current')
ciscoAAAServerCapabilityMDS13R1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 129, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoAAAServerCapabilityMDS13R1 = ciscoAAAServerCapabilityMDS13R1.setProductRelease('Cisco MDS 1.3(1)')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoAAAServerCapabilityMDS13R1 = ciscoAAAServerCapabilityMDS13R1.setStatus('current')
ciscoAAAServerCapabilityACSWV03R000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 129, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoAAAServerCapabilityACSWV03R000 = ciscoAAAServerCapabilityACSWV03R000.setProductRelease('ACSW (Application Control Software) 3.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoAAAServerCapabilityACSWV03R000 = ciscoAAAServerCapabilityACSWV03R000.setStatus('current')
ciscoAAAServerCapc4710aceVA1R70 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 129, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoAAAServerCapc4710aceVA1R70 = ciscoAAAServerCapc4710aceVA1R70.setProductRelease('ACSW (Application Control Software) A1(7)\n                         for ACE 4710 Application Control Engine \n                         Appliance.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoAAAServerCapc4710aceVA1R70 = ciscoAAAServerCapc4710aceVA1R70.setStatus('current')
mibBuilder.exportSymbols("CISCO-AAA-SERVER-CAPABILITY", PYSNMP_MODULE_ID=ciscoAAAServerCapability, ciscoAAAServerCapabilityACSWV03R000=ciscoAAAServerCapabilityACSWV03R000, ciscoAAAServerCapc4710aceVA1R70=ciscoAAAServerCapc4710aceVA1R70, ciscoAAAServerCapability=ciscoAAAServerCapability, ciscoAAAServerCapabilityMDS13R1=ciscoAAAServerCapabilityMDS13R1, ciscoAAAServerCapabilityV10R00=ciscoAAAServerCapabilityV10R00)
