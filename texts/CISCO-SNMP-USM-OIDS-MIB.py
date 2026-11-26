#
# PySNMP MIB module CISCO-SNMP-USM-OIDS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-SNMP-USM-OIDS-MIB
# Produced by pysmi-1.1.12 at Thu Nov 26 06:07:45 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ciscoModules, = mibBuilder.importSymbols("CISCO-SMI", "ciscoModules")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ModuleIdentity, MibIdentifier, iso, Counter32, IpAddress, Integer32, NotificationType, ObjectIdentity, Unsigned32, Bits, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "ModuleIdentity", "MibIdentifier", "iso", "Counter32", "IpAddress", "Integer32", "NotificationType", "ObjectIdentity", "Unsigned32", "Bits", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoSnmpUsmOidsMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 12, 6))
ciscoSnmpUsmOidsMIB.setRevisions(('2006-02-28 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoSnmpUsmOidsMIB.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoSnmpUsmOidsMIB.setLastUpdated('200602280000Z')
if mibBuilder.loadTexts: ciscoSnmpUsmOidsMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoSnmpUsmOidsMIB.setContactInfo('       Cisco Systems\n                        Customer Service\n\n                Postal: 170 W. Tasman Drive\n                        San Jose, CA 95134\n                        USA\n\n                   Tel: +1 800 553-NETS\n\n                E-mail: cs-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoSnmpUsmOidsMIB.setDescription("This MIB extends the OID's for SNMP-USM-MIB\n                 specified in RFC 3414.\n\n                The privacy protocol OID's specified herein \n                are intended to be used as values  for \n                usmUserPrivProtocol when managing SNMPv3  \n                users via the snmpUsmMIB.\n\n                This MIB defines the OID's for the following\n                encryption options:\n\n                        * 192 bit key size AES\n                        * 256 bit key size AES\n                        * 168 bit key size 3DES.\n\n                OID for 128 bit key size AES encryption is \n                defined in SNMP-USM-AES-MIB as per the \n                RFC 3826.")
ciscoSnmpPrivProtocols = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 12, 6, 1))
cusmAESCfb192PrivProtocol = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 12, 6, 1, 1))
cusmAESCfb256PrivProtocol = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 12, 6, 1, 2))
cusm3DES168PrivProtocol = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 12, 6, 1, 3))
mibBuilder.exportSymbols("CISCO-SNMP-USM-OIDS-MIB", ciscoSnmpPrivProtocols=ciscoSnmpPrivProtocols, cusmAESCfb192PrivProtocol=cusmAESCfb192PrivProtocol, ciscoSnmpUsmOidsMIB=ciscoSnmpUsmOidsMIB, cusm3DES168PrivProtocol=cusm3DES168PrivProtocol, cusmAESCfb256PrivProtocol=cusmAESCfb256PrivProtocol, PYSNMP_MODULE_ID=ciscoSnmpUsmOidsMIB)
