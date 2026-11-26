#
# PySNMP MIB module CISCO-ENHANCED-SLB-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-ENHANCED-SLB-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 26 06:06:58 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Counter64, TimeTicks, NotificationType, Integer32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, IpAddress, Bits, Gauge32, Unsigned32, MibIdentifier, Counter32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "NotificationType", "Integer32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "IpAddress", "Bits", "Gauge32", "Unsigned32", "MibIdentifier", "Counter32", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoEnhancedSlbCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 507))
ciscoEnhancedSlbCapability.setRevisions(('2008-07-07 00:00', '2008-02-08 00:00', '2006-05-22 00:00',))
if mibBuilder.loadTexts: ciscoEnhancedSlbCapability.setLastUpdated('200807070000Z')
if mibBuilder.loadTexts: ciscoEnhancedSlbCapability.setOrganization('Cisco Systems, Inc.')
ciscoEnhancedSlbCapACSWV03R000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 507, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEnhancedSlbCapACSWV03R000 = ciscoEnhancedSlbCapACSWV03R000.setProductRelease('ACSW (Application Control Software) 3.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEnhancedSlbCapACSWV03R000 = ciscoEnhancedSlbCapACSWV03R000.setStatus('current')
ciscoEnhancedSlbCapc4710aceVA1R70 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 507, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEnhancedSlbCapc4710aceVA1R70 = ciscoEnhancedSlbCapc4710aceVA1R70.setProductRelease('ACSW (Application Control Software) A1(7)\n                    for ACE 4710 Application Control Engine \n                    Appliance')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEnhancedSlbCapc4710aceVA1R70 = ciscoEnhancedSlbCapc4710aceVA1R70.setStatus('current')
ciscoEnhancedSlbCapc4710aceVA3R10 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 507, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEnhancedSlbCapc4710aceVA3R10 = ciscoEnhancedSlbCapc4710aceVA3R10.setProductRelease('ACSW (Application Control Software) A3(1.0)\n                    for ACE 4710 Application Control Engine \n                    Appliance')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEnhancedSlbCapc4710aceVA3R10 = ciscoEnhancedSlbCapc4710aceVA3R10.setStatus('current')
mibBuilder.exportSymbols("CISCO-ENHANCED-SLB-CAPABILITY", PYSNMP_MODULE_ID=ciscoEnhancedSlbCapability, ciscoEnhancedSlbCapACSWV03R000=ciscoEnhancedSlbCapACSWV03R000, ciscoEnhancedSlbCapability=ciscoEnhancedSlbCapability, ciscoEnhancedSlbCapc4710aceVA3R10=ciscoEnhancedSlbCapc4710aceVA3R10, ciscoEnhancedSlbCapc4710aceVA1R70=ciscoEnhancedSlbCapc4710aceVA1R70)
